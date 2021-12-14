import logging
from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

from recipes.domain.exceptions.recipe_not_found import RecipeNotFound


def custom_exception_handler(exception, context):
    response = exception_handler(exception, context)

    if isinstance(exception, RecipeNotFound):
        error_data = {
            'error_msg': str(exception),
            'error_code': 'not_found'
        }

        #logging.error(f"Original error detail and callstack: {exception}")

        return Response(
            data=error_data,
            status=status.HTTP_404_NOT_FOUND
        )

    return response
