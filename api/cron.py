from .models import Message, Room, Community, Prompt, generate_unique_code
import random


def update_prompts():
    communities = Community.objects.all()
    for community in communities:
        prompts = community.prompts.all()
        community.currentPrompt = random.randint(prompts[0,len(prompts) - 1].body)
        community.save()