import logging

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema

import constants
from response_utils import ApiResponse, get_error_message
from users.models import User
from users.serializers import UserSerializer

logger = logging.getLogger('django')


class UsersList(APIView):
    """
    Class is used for list all the user or create new user.
    """
    authentication_classes = []
    permission_classes = []

    @swagger_auto_schema(operation_description="Api is used to get all user detail"
                                               "from the application",
                         responses={200: UserSerializer()})
    def get(self, request):
        """
        Function is used to get all the user list.
        :param request: request header with required info.
        :return: user list
        """
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        api_response = ApiResponse(status=1, data=serializer.data, message=constants.USERS_GET_SUCCESS,
                                   http_status=status.HTTP_200_OK)
        return api_response.create_response()

    @swagger_auto_schema(request_body=UserSerializer, operation_description="API is used to post the user detail "
                                                                            "and store data inside database")
    def post(self, request):
        """
        Function is used to create new object or value in table and return status.
        :param request: request header with user info for creating new object.
        :return: user info
        """
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            api_response = ApiResponse(status=1, data=serializer.data, message=constants.CREATE_USER_SUCCESS,
                                       http_status=status.HTTP_201_CREATED)
            return api_response.create_response()
        api_response = ApiResponse(status=0, message=get_error_message(serializer),
                                   http_status=status.HTTP_400_BAD_REQUEST)
        return api_response.create_response()


class UserDetails(APIView):
    """
    Class is used for retrieve, update or delete a user instance.
    """
    permission_classes = [IsAuthenticated, ]

    @swagger_auto_schema(operation_description="Api is used to get particular user detail"
                                               "from the application",
                         responses={200: UserSerializer()})
    def get(self, request, pk):
        """
        Function is used for get user info with pk
        :param request: request header with required info.
        :param pk: primary key of a object.
        :return: user info or send proper error status
        """
        try:
            user = User.objects.get(id=pk)
        except User.DoesNotExist as e:
            logger.exception(e)
            api_response = ApiResponse(status=0, message=constants.USER_DOES_NOT_EXIST,
                                       http_status=status.HTTP_404_NOT_FOUND)
            return api_response.create_response()
        serializer = UserSerializer(user)
        api_response = ApiResponse(status=1, data=serializer.data, message=constants.GET_USER_SUCCESS,
                                   http_status=status.HTTP_200_OK)
        return api_response.create_response()
