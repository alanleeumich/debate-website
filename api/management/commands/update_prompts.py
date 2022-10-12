from django.core.management.base import BaseCommand, CommandError

from api.models import Message, Room, Community, Prompt, generate_unique_code
import random

class Command(BaseCommand):
    def handle(self, *args, **options):
        communities = Community.objects.all()
        for community in communities:
            prompts = community.prompts.all()
            community.currentPrompt = prompts[random.randint(0,prompts.count())].body
            community.save()
        
        return