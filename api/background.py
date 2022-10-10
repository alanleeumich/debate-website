
from .models import Community, Prompt
from background_task import background
import random



@background(schedule=5)
def cyclePrompts():
    print("CYCLING PROMPTS")
    communities = Community.objects.all()
    for community in communities:
        prompts = community.prompts.all()
        community.currentPrompt = prompts[random.randint(0,prompts.count() - 1)].body
        community.save()
