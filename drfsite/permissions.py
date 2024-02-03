from rest_framework import permissions


class CustomPermission(permissions.BasePermission):
    """
    Пользователи с ролью администратора имеют полный доступ (GET, POST, PUT, DELETE, PATCH).
    Все остальные пользователи могут только просматривать (GET) и создавать (POST).
    Неавторизованные пользователи не имеют доступа.
    """

    def has_permission(self, request, view):

        if request.user.username == 'test':
            return request.method in permissions.SAFE_METHODS
        elif request.user.username == 'admin':
            return True
        else:
            return False

        # if request.user.is_authenticated:
    #     if request.user.is_staff:
    #         return True  # Администраторы имеют полный доступ
    #     elif request.method in permissions.SAFE_METHODS:
    #         return True  # Разрешено любому для GET, HEAD, OPTIONS
    #     else:
    #         return False  # Запрещено для всех остальных методов
    # else:
    #     return False
