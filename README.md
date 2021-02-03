# Akibox Tutorial - Django REST Framework

This is a tutorial project to help you get to know the Akita/Django
integration.  It contains a server built using Django REST Framework that
implements a toy Dropbox-like file server.

You can use Akita to generate a spec describing the Akibox APIs.  Normally, you
would do this by starting the Akita Client and sending traffic to the server --
the Akita Client captures network traffic, which it uses to build a spec.

But how to generate API traffic?  You could send requests manually, but you may
also have another good source of traffic -- integration tests!  Django offers
handy testing tools that avoid starting a server and sending traffic over the
network, but that means the normal Akita method of packet capture won't work. 

The Akita/Django integration lets you use integration tests you've written for
your Django application as the source of API traffic that Akita will use to
build the spec.  It works by wrapping the Django test client with an extra
layer that captures requests and responses and sends them to Akita.

## Running the Server

```bash
python manage.py runserver
```
