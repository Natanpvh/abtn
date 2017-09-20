from django.contrib import admin

# Register your models here.

from associacao.models import Categoria, Post, ImagenDoPost, SlideDoSite, LinkImportante, Video
from image_cropping import ImageCroppingMixin


class CategoriaAdmin(admin.ModelAdmin):
    """
    Exibe categorias de posts do site
    """
    list_per_page = 10
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')


class ImagenDoPostAdmin(admin.TabularInline):
    model = ImagenDoPost
    extra = 1


class PostAdmin(admin.ModelAdmin):
    """
    Exibição e configurações para o gerenciamente
    de Postangens no admin do site
    """
    list_per_page = 10
    list_display = ('id', 'titulo', 'categoria', 'autor', 'status', 'criado')
    list_display_links = ('titulo', 'autor')
    search_fields = ('titulo', 'categoria__nome', 'status')
    list_filter = ['categoria__nome', 'titulo', 'criado']
    prepopulated_fields = {'slug': ("titulo",)}
    inlines = [ImagenDoPostAdmin]

    fieldsets = (
        ('Conteudo do Post', {
            'fields': [
                'titulo',
                'slug',
                'texto',
                'categoria',
                'autor',
                'status'
            ], 'classes': ['grp-collapse grp-open']}),
    )


class FotoAdmin(admin.ModelAdmin):
    """
    Gerenciamento e exibição de imagens dos posts
    """
    list_per_page = 10
    list_display = ('id', 'titulo_img', 'foto_thumbnail', 'post_imagem_id')

    def foto_thumbnail(self, object):
        try:
            return '<img height="50px" src="/media/%s"/>' % (object.imagem)
        except:
            return "Sem Imagem"

    foto_thumbnail.short_description = 'Imagem'
    foto_thumbnail.allow_tags = True


class SlideDoSiteAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ('id', 'titulo_slide', 'foto_thumbnail', 'status', 'url_slide')
    list_display_links = ('titulo_slide', 'foto_thumbnail')

    def foto_thumbnail(self, object):
        try:
            return '<img height="50px" src="/media/%s"/>' % (object.image)
        except:
            return "Sem Imagem"

    foto_thumbnail.short_description = 'Imagem'
    foto_thumbnail.allow_tags = True


class LinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo_link', 'url_link')


class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo_video', 'video_play')

    def video_play(self, object):
        try:
            return '<iframe width="200" src="%s" frameborder="0"></iframe>' % (object.url_video)
        except:
            return "Sem video"

    video_play.short_description = 'Video'
    video_play.allow_tags = True


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(ImagenDoPost, FotoAdmin)
admin.site.register(SlideDoSite, SlideDoSiteAdmin)
admin.site.register(LinkImportante, LinkAdmin)
admin.site.register(Video, VideoAdmin)
