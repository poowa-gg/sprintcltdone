import click
from weather_api import weather_api_client
from farmer_manager import farmer_manager
from alert_manager import alert_manager
from feedback_manager import feedback_manager
import json

@click.group()
def cli():
    """Climatovate Farmer Weather Alert System - Sprint 1 CLI"""
    pass

@cli.group()
def forecast():
    """Weather forecast operations"""
    pass

@forecast.command('query')
@click.argument('lat', type=float)
@click.argument('lon', type=float)
@click.option('--days', default=3, help='Number of days to forecast')
def forecast_query(lat, lon, days):
    """Query weather API for a test location"""
    try:
        click.echo(f"Querying forecast for location: {lat}, {lon}")
        data = weather_api_client.get_hyperlocal_forecast(lat, lon, days)
        click.echo(json.dumps(data, indent=2))
    except Exception as e:
        click.echo(f"Error: {str(e)}", err=True)

@cli.group()
def farmer():
    """Farmer management operations"""
    pass

@farmer.command('enroll')
@click.argument('phone')
@click.argument('lat', type=float)
@click.argument('lon', type=float)
def farmer_enroll(phone, lat, lon):
    """Enroll a new farmer"""
    try:
        farmer_id = farmer_manager.enroll_farmer(phone, lat, lon)
        click.echo(f"✓ Farmer enrolled successfully!")
        click.echo(f"Farmer ID: {farmer_id}")
        click.echo(f"Phone: {phone}")
        click.echo(f"Location: {lat}, {lon}")
    except Exception as e:
        click.echo(f"Error: {str(e)}", err=True)

@farmer.command('list')
def farmer_list():
    """List all enrolled farmers"""
    try:
        farmers = farmer_manager.get_all_farmers()
        if not farmers:
            click.echo("No farmers enrolled yet.")
            return
        
        click.echo(f"\nTotal farmers: {len(farmers)}\n")
        for f in farmers:
            click.echo(f"ID: {f.farmer_id}")
            click.echo(f"Phone: {f.phone_number}")
            click.echo(f"Location: {f.lat}, {f.lon}")
            click.echo(f"Enrolled: {f.enrollment_date}")
            click.echo("-" * 50)
    except Exception as e:
        click.echo(f"Error: {str(e)}", err=True)

@cli.group()
def alert():
    """Alert management operations"""
    pass

@alert.command('generate')
def alert_generate():
    """Generate alerts for all farmers"""
    try:
        click.echo("Generating alerts for all farmers...")
        alerts = alert_manager.generate_alerts_for_all_farmers()
        click.echo(f"✓ Generated {len(alerts)} alert(s)")
        
        for a in alerts:
            click.echo(f"\nAlert ID: {a.alert_id}")
            click.echo(f"Farmer ID: {a.farmer_id}")
            click.echo(f"Type: {a.peril_type}")
            click.echo(f"Severity: {a.severity}")
            click.echo("-" * 50)
    except Exception as e:
        click.echo(f"Error: {str(e)}", err=True)

@alert.command('review')
def alert_review():
    """Review pending alerts"""
    try:
        alerts = alert_manager.get_pending_alerts()
        if not alerts:
            click.echo("No pending alerts.")
            return
        
        click.echo(f"\nPending alerts: {len(alerts)}\n")
        for a in alerts:
            farmer = farmer_manager.get_farmer(a.farmer_id)
            click.echo(f"Alert ID: {a.alert_id}")
            click.echo(f"Farmer Phone: {farmer.phone_number}")
            click.echo(f"Message:\n{a.message}")
            click.echo("=" * 50)
    except Exception as e:
        click.echo(f"Error: {str(e)}", err=True)

@alert.command('mark-delivered')
@click.argument('alert_id')
def alert_mark_delivered(alert_id):
    """Mark an alert as delivered"""
    try:
        alert_manager.mark_alert_delivered(alert_id)
        click.echo(f"✓ Alert {alert_id} marked as delivered")
    except Exception as e:
        click.echo(f"Error: {str(e)}", err=True)

@cli.group()
def feedback():
    """Feedback management operations"""
    pass

@feedback.command('add')
@click.argument('farmer_id')
@click.argument('text')
@click.option('--cost-saving', is_flag=True, help='Mark as cost-saving feedback')
def feedback_add(farmer_id, text, cost_saving):
    """Record farmer feedback"""
    try:
        feedback_id = feedback_manager.record_feedback(farmer_id, text, cost_saving)
        click.echo(f"✓ Feedback recorded successfully!")
        click.echo(f"Feedback ID: {feedback_id}")
        if cost_saving:
            click.echo("✓ Marked as cost-saving")
    except Exception as e:
        click.echo(f"Error: {str(e)}", err=True)

@feedback.command('list')
def feedback_list():
    """List all feedback"""
    try:
        feedbacks = feedback_manager.get_all_feedback()
        if not feedbacks:
            click.echo("No feedback recorded yet.")
            return
        
        click.echo(f"\nTotal feedback: {len(feedbacks)}\n")
        cost_saving_count = sum(1 for f in feedbacks if f.cost_saving_indicator)
        click.echo(f"Cost-saving feedback: {cost_saving_count}\n")
        
        for fb in feedbacks:
            click.echo(f"Feedback ID: {fb.feedback_id}")
            click.echo(f"Farmer ID: {fb.farmer_id}")
            click.echo(f"Text: {fb.feedback_text}")
            click.echo(f"Cost-saving: {'Yes' if fb.cost_saving_indicator else 'No'}")
            click.echo(f"Date: {fb.feedback_date}")
            click.echo("-" * 50)
    except Exception as e:
        click.echo(f"Error: {str(e)}", err=True)

if __name__ == '__main__':
    cli()
