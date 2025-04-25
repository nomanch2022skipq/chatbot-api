from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth import authenticate, logout as auth_logout
from django.contrib.auth.views import LoginView as AuthLoginView
from django.http import JsonResponse
from django.shortcuts import redirect
from django.views import View
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authentication import BasicAuthentication
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class CustomLoginView(AuthLoginView):
    template_name = "authentication/login.html"
    redirect_authenticated_user = True


class CustomLogoutView(View):
    http_method_names = ["get", "post"]
    next_page = "/swagger/"

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        next_page = request.GET.get("next", self.next_page)
        return redirect(next_page)

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)


class LoginView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = [BasicAuthentication]

    @swagger_auto_schema(
        operation_description="Login with username and password to get JWT tokens",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["username", "password"],
            properties={
                "username": openapi.Schema(
                    type=openapi.TYPE_STRING, description="Username"
                ),
                "password": openapi.Schema(
                    type=openapi.TYPE_STRING, description="Password"
                ),
            },
        ),
        responses={
            200: openapi.Response(
                description="Login Successful",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "user": openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            properties={
                                "id": openapi.Schema(type=openapi.TYPE_INTEGER),
                                "username": openapi.Schema(type=openapi.TYPE_STRING),
                                "email": openapi.Schema(type=openapi.TYPE_STRING),
                            },
                        ),
                        "tokens": openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            properties={
                                "refresh_token": openapi.Schema(
                                    type=openapi.TYPE_STRING
                                ),
                                "access_token": openapi.Schema(
                                    type=openapi.TYPE_STRING
                                ),
                            },
                        ),
                    },
                ),
            ),
            401: "Invalid credentials",
        },
    )
    def post(self, request):
        if hasattr(request, "user") and request.user.is_authenticated:
            user = request.user
        else:
            username = request.data.get("username")
            password = request.data.get("password")
            user = authenticate(username=username, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    "user": {
                        "id": user.id,
                        "username": user.username,
                        "email": user.email,
                    },
                    "tokens": {
                        "refresh_token": str(refresh),
                        "access_token": str(refresh.access_token),
                    },
                }
            )
        return Response(
            {"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
        )


class RegisterView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Register a new user",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["username", "password"],
            properties={
                "username": openapi.Schema(
                    type=openapi.TYPE_STRING, description="Username for the new account"
                ),
                "email": openapi.Schema(
                    type=openapi.TYPE_STRING, description="Email address (optional)"
                ),
                "password": openapi.Schema(
                    type=openapi.TYPE_STRING, description="Password for the account"
                ),
            },
        ),
        responses={
            201: openapi.Response(
                description="Registration Successful",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "user": openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            properties={
                                "id": openapi.Schema(type=openapi.TYPE_INTEGER),
                                "username": openapi.Schema(type=openapi.TYPE_STRING),
                                "email": openapi.Schema(type=openapi.TYPE_STRING),
                            },
                        ),
                        "tokens": openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            properties={
                                "refresh": openapi.Schema(type=openapi.TYPE_STRING),
                                "access": openapi.Schema(type=openapi.TYPE_STRING),
                            },
                        ),
                    },
                ),
            ),
            400: "Bad Request - Invalid data",
        },
    )
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    "user": serializer.data,
                    "tokens": {
                        "refresh": str(refresh),
                        "access": str(refresh.access_token),
                    },
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            # Handle JWT token blacklisting
            refresh_token = request.data.get("refresh")
            if refresh_token:
                token = RefreshToken(refresh_token)
                token.blacklist()

            # Handle session logout
            auth_logout(request)

            return Response(
                {"message": "Successfully logged out"}, status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST
            )
