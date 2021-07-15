from django.db import models

#### Project activity list
activity_list = (
    ('completed', 'completed'),
    ('ongoing', 'ongoing'),
    ('stalled', 'stalled'),
)

##### Team Model ######
class Team(models.Model):
    name = models.CharField(max_length=400)
    title = models.CharField(max_length=400)
    description = models.TextField()
    image = models.ImageField(upload_to="photos/", )

    def __str__(self) -> str:
        return self.name


############# Project Model ##################
class Project(models.Model):
    title = models.CharField(max_length=400)
    timestamp = models.DateTimeField(auto_now_add=True)
    activity_list = models.CharField(max_length=50, choices=activity_list)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self) -> str:
        return self.title


