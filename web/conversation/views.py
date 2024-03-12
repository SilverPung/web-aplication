from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from item.models import Item
from .models import Conversation,ConversationMessage
from .forms import NewConversationForm
from django.db.models import Q
# Create your views here.

@login_required
def new_conversations(request,item_pk):
    item=get_object_or_404(Item,pk=item_pk)
    if item.created_by==request.user:
       return redirect('item:detail',pk=item_pk)

    conversations = Conversation.objects.filter(item=item, members__in=[request.user.id])

    if conversations:
        return redirect('conversation:detail', conversation_pk=conversations[0].pk)
    
    if request.method == 'POST':
        form = NewConversationForm(request.POST)
        if form.is_valid():
            conversation= Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()

            conversation_massage=form.save(commit=False)
            conversation_massage.conversation=conversation
            conversation_massage.created_by=request.user
            conversation_massage.save()
            return redirect('item:detail',pk=item_pk)
    else:
        form=NewConversationForm()

    return render(request, 'conversation/new.html', {'form':form})

@login_required
def inbox(request):
    conversations = Conversation.objects.filter(members__in=[request.user.id])
    return render(request, 'conversation/inbox.html', {'conversations':conversations})

@login_required
def detail(request, conversation_pk):
    conversation=Conversation.objects.filter(members__in=[request.user.id]).get(pk=conversation_pk)
    
    if request.method == 'POST':
        form=NewConversationForm(request.POST)
        if form.is_valid():
            conversation_massage=form.save(commit=False)
            conversation_massage.conversation=conversation
            conversation_massage.created_by=request.user
            conversation_massage.save()

            conversation.save()
            return redirect('conversation:detail',conversation_pk=conversation_pk)
        
    else:
        form=NewConversationForm()

    return render(request, 'conversation/detail.html', {'conversation':conversation, 'form':form})