from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    # Returns 10 elements per page by default
    page_size = 10
    page_query_param = "page"
    page_size_query_param = "limit"
