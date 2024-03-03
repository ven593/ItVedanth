from django.shortcuts import render, redirect
from .models import Message, Comment, Like,LikeComment
from .forms import MessageForm, CommentForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse


def feed(request):
    messages = Message.objects.all().order_by('-created_at')
    return render(request, 'fd.html', {'messages': messages})


def post_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        # message = Message()
        if form.is_valid():
            message = form.save(commit=False)
            message.user = request.user
            message.save()
            return redirect('feed')
    else:
        form = MessageForm()
    return render(request, 'pm.html', {'form': form})


@login_required
def message_list(request):
    messages = Message.objects.all()
    return render(request, 'message_list.html', {'messages': messages})


@login_required
def post_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.user = request.user
            message.save()
            return redirect('message_list')
    else:
        form = MessageForm()
    return render(request, 'post_message.html', {'form': form})


@login_required
def post_comment(request, message_id):
    message = Message.objects.get(pk=message_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.message = message
            comment.save()
            return redirect('message_list')
    else:
        form = CommentForm()
        return render(request, 'post_comment.html', {'form': form, 'message': message})
    context = {'message_id': message_id}
    return render(request, 'post_comment.html', context)


@login_required
def delete_message(request, message_id):
    message = Message.objects.get(pk=message_id)
    if request.user == message.user:
        message.delete()
    return redirect('message_list')


@login_required
def like_message(request, message_id):
    message = get_object_or_404(Message, pk=message_id)

    # Check if the user has already liked the message
    like, created = Like.objects.get_or_create(user=request.user, message=message)

    if not created:
        # User has already liked the message, remove the like
        like.delete()
    else:
        # User has not liked the message, add the like
        message.likes.add(like)

    return HttpResponseRedirect(reverse('message_list'))  # Redirect to your message list view


@login_required
def like_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)

    # Check if the user has already liked the comment
    like, created = Like.objects.get_or_create(user=request.user, comment=comment)
    if like in comment.likes.all():
        comment.likes.remove(like)
    else:
        comment.likes.add(like)
        # Retrieve the comment
        comment = Comment.objects.get(pk=comment_id)

        # Assuming Comment model has a ForeignKey to Message model
        message_id = comment.message.id

        # Your logic to handle the like
        # Ensure you're providing the correct message_id when saving the like
        LikeComment.objects.create(message_id=message_id, comment=comment, user=request.user)
    if not created:
        # User has already liked the comment, remove the like
        like.delete()
    else:
        # User has not liked the comment, add the like
        comment.likes.add(like)
    # return HttpResponseRedirect(reverse('comment_list'))
    return HttpResponseRedirect(reverse('message_list'))  # Redirect to your message list view

