from dal import autocomplete

from blog.models import Category, Tag, Post  # Status


class CategoryAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Category.objects.none()

        # qs = Category.objects.filter(owner=self.request.user)
        qs = Category.objects.all()
        # print(qs, '*'*20)

        if self.q:
            qs = qs.filter(name__istartswith=self.q)
        return qs


class TagAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Tag.objects.none()

        # qs = Tag.objects.filter(owner=self.request.user)
        qs = Tag.objects.all()
        # print(qs, '*'*50)

        if self.q:
            qs = qs.filter(name__istartswith=self.q)
        return qs


# class StatusAutocomplete(autocomplete.Select2QuerySetView):
#     def get_queryset(self):
#         if not self.request.user.is_authenticated:
#             return Post.objects.none()
#
#         # qs = Tag.objects.filter(owner=self.request.user)
#         qs = Post.status
#
#         if self.q:
#             qs = qs.filter(name__istartswith=self.q)
#         return qs
