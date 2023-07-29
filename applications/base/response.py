from rest_framework import status
from rest_framework.response import Response


operation_success = Response(status=status.HTTP_200_OK, data={"message": "OPERATION_SUCCESS"})
operation_failure = Response(status=status.HTTP_400_BAD_REQUEST, data={"message": "OPERATION_FAILURE"})
