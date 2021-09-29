from posts.models import Comment, Follow, Group, Post, User
from rest_framework import serializers
from rest_framework.generics import get_object_or_404
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class FollowSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=True
    )
    following = SlugRelatedField(
        slug_field='username',
        required=True,
        queryset=User.objects.all()
    )

    class Meta:
        fields = '__all__'
        model = Follow

        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following', )
            )
        ]

    def validate(self, data):
        get_object_or_404(User, username=data['following'])
        if self.context['request'].user == data['following']:
            raise serializers.ValidationError('Сам на себя подписываешься!')
        exist_follow = Follow.objects.filter(
            user=self.context['request'].user,
            following=data['following']
        )
        if exist_follow:
            raise serializers.ValidationError('Уже подписан')
        return data


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"
