from django.contrib import admin
from .models import User, Team, Activity, Leaderboard, Workout


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'team', 'created_at']
    search_fields = ['username', 'email']
    list_filter = ['team', 'created_at']


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created_at']
    search_fields = ['name']
    list_filter = ['created_at']


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'activity_type', 'duration', 'calories', 'date']
    search_fields = ['user_id', 'activity_type']
    list_filter = ['activity_type', 'date']


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ['username', 'team', 'total_activities', 'total_calories', 'rank']
    search_fields = ['username', 'team']
    list_filter = ['team']
    ordering = ['rank']


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ['name', 'activity_type', 'duration', 'difficulty', 'calories_estimate']
    search_fields = ['name', 'activity_type']
    list_filter = ['difficulty', 'activity_type']
