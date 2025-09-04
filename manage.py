#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    # """Added by ngrok"""
    # # This block handles 'make rundjangosite' which uses this manage.py as the entry point.
    # # Set env variable to protect against the autoreloader.
    # if os.getenv("NGROK_LISTENER_RUNNING") is None:
    #     os.environ["NGROK_LISTENER_RUNNING"] = "true"
    #     from pyngrok import ngrok

    #     def setup():
    #         listen = sys.argv[2] if len(sys.argv) > 2 else "localhost:8000"
    #         ngrok.set_auth_token("2YGWIwetsgBQBGLTc4CM6lhWmPs_7vcCeB3MijthzYG3CMdLe")
            
    #         ngrok.connect(8000)
    #         with open("public_url.txt","w+") as f :

    #             f.write(ngrok.get_tunnels()[0].public_url)
            
    #         print(f"Forwarding to {listen} from ingress url: {ngrok.get_tunnels()[0].public_url}")
    #         # listener.forward(listen)

    #     setup()
    """End added by ngrok"""
    """Run administrative tasks."""

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'livemanga.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()

    

