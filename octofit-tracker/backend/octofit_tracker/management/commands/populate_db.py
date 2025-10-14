from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Starting database population...'))

        # Delete existing data
        self.stdout.write('Deleting existing data...')
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        self.stdout.write('Creating teams...')
        team_marvel = Team.objects.create(
            name='Team Marvel',
            description='Marvel Super Heroes',
            members=['Iron Man', 'Captain America', 'Thor', 'Black Widow', 'Hulk']
        )
        
        team_dc = Team.objects.create(
            name='Team DC',
            description='DC Super Heroes',
            members=['Superman', 'Batman', 'Wonder Woman', 'Flash', 'Aquaman']
        )

        # Create Users - Team Marvel
        self.stdout.write('Creating users...')
        users_marvel = [
            User.objects.create(
                username='ironman',
                email='tony@stark.com',
                password='arc_reactor',
                team='Team Marvel'
            ),
            User.objects.create(
                username='captainamerica',
                email='steve@avengers.com',
                password='shield123',
                team='Team Marvel'
            ),
            User.objects.create(
                username='thor',
                email='thor@asgard.com',
                password='mjolnir',
                team='Team Marvel'
            ),
            User.objects.create(
                username='blackwidow',
                email='natasha@shield.com',
                password='widow_bite',
                team='Team Marvel'
            ),
            User.objects.create(
                username='hulk',
                email='bruce@gamma.com',
                password='smash123',
                team='Team Marvel'
            ),
        ]

        # Create Users - Team DC
        users_dc = [
            User.objects.create(
                username='superman',
                email='clark@dailyplanet.com',
                password='krypton',
                team='Team DC'
            ),
            User.objects.create(
                username='batman',
                email='bruce@wayneenterprises.com',
                password='gotham_knight',
                team='Team DC'
            ),
            User.objects.create(
                username='wonderwoman',
                email='diana@themyscira.com',
                password='lasso_truth',
                team='Team DC'
            ),
            User.objects.create(
                username='flash',
                email='barry@starlabs.com',
                password='speed_force',
                team='Team DC'
            ),
            User.objects.create(
                username='aquaman',
                email='arthur@atlantis.com',
                password='trident123',
                team='Team DC'
            ),
        ]

        all_users = users_marvel + users_dc

        # Create Activities
        self.stdout.write('Creating activities...')
        activity_types = ['Running', 'Swimming', 'Cycling', 'Boxing', 'Yoga', 'Weightlifting']
        
        for i, user in enumerate(all_users):
            for j in range(5):  # 5 activities per user
                Activity.objects.create(
                    user_id=str(user._id),
                    activity_type=activity_types[(i + j) % len(activity_types)],
                    duration=30 + (j * 10),
                    distance=5.0 + (j * 2.0) if (i + j) % 2 == 0 else None,
                    calories=200 + (j * 50),
                    date=timezone.now() - timedelta(days=j)
                )

        # Create Leaderboard entries
        self.stdout.write('Creating leaderboard entries...')
        leaderboard_data = [
            {'user': users_marvel[0], 'activities': 25, 'duration': 1500, 'calories': 15000, 'rank': 1},
            {'user': users_dc[0], 'activities': 23, 'duration': 1400, 'calories': 14500, 'rank': 2},
            {'user': users_marvel[1], 'activities': 22, 'duration': 1350, 'calories': 14000, 'rank': 3},
            {'user': users_dc[1], 'activities': 21, 'duration': 1300, 'calories': 13500, 'rank': 4},
            {'user': users_marvel[2], 'activities': 20, 'duration': 1250, 'calories': 13000, 'rank': 5},
            {'user': users_dc[2], 'activities': 19, 'duration': 1200, 'calories': 12500, 'rank': 6},
            {'user': users_marvel[3], 'activities': 18, 'duration': 1150, 'calories': 12000, 'rank': 7},
            {'user': users_dc[3], 'activities': 17, 'duration': 1100, 'calories': 11500, 'rank': 8},
            {'user': users_marvel[4], 'activities': 16, 'duration': 1050, 'calories': 11000, 'rank': 9},
            {'user': users_dc[4], 'activities': 15, 'duration': 1000, 'calories': 10500, 'rank': 10},
        ]

        for data in leaderboard_data:
            Leaderboard.objects.create(
                user_id=str(data['user']._id),
                username=data['user'].username,
                team=data['user'].team,
                total_activities=data['activities'],
                total_duration=data['duration'],
                total_calories=data['calories'],
                rank=data['rank']
            )

        # Create Workouts
        self.stdout.write('Creating workouts...')
        workouts_data = [
            {
                'name': 'Hero HIIT',
                'description': 'High-intensity interval training for super heroes',
                'activity_type': 'HIIT',
                'duration': 30,
                'difficulty': 'Hard',
                'calories_estimate': 400
            },
            {
                'name': 'Power Yoga',
                'description': 'Yoga session to improve flexibility and strength',
                'activity_type': 'Yoga',
                'duration': 45,
                'difficulty': 'Medium',
                'calories_estimate': 250
            },
            {
                'name': 'Speed Run',
                'description': 'Fast-paced running workout',
                'activity_type': 'Running',
                'duration': 60,
                'difficulty': 'Hard',
                'calories_estimate': 600
            },
            {
                'name': 'Strength Training',
                'description': 'Build muscle and power',
                'activity_type': 'Weightlifting',
                'duration': 50,
                'difficulty': 'Hard',
                'calories_estimate': 350
            },
            {
                'name': 'Combat Training',
                'description': 'Boxing and martial arts workout',
                'activity_type': 'Boxing',
                'duration': 40,
                'difficulty': 'Hard',
                'calories_estimate': 450
            },
            {
                'name': 'Aqua Fitness',
                'description': 'Swimming and water exercises',
                'activity_type': 'Swimming',
                'duration': 45,
                'difficulty': 'Medium',
                'calories_estimate': 350
            },
            {
                'name': 'Cycling Adventure',
                'description': 'Long-distance cycling workout',
                'activity_type': 'Cycling',
                'duration': 90,
                'difficulty': 'Medium',
                'calories_estimate': 700
            },
        ]

        for workout_data in workouts_data:
            Workout.objects.create(**workout_data)

        # Summary
        self.stdout.write(self.style.SUCCESS('\n=== Database Population Complete ==='))
        self.stdout.write(self.style.SUCCESS(f'Teams created: {Team.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'Users created: {User.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'Activities created: {Activity.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'Leaderboard entries: {Leaderboard.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'Workouts created: {Workout.objects.count()}'))
        self.stdout.write(self.style.SUCCESS('\nDatabase populated successfully with superhero test data! 🦸‍♂️🦸‍♀️'))
