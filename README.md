# MIDDLEWARE

# In Python Django, **Middleware** is a framework to process request and responses globally before they are processed by the view or after they leave the view.

Middleware components are designed so that  they remain between webserver and the view , allowing us to perform various operations on requests and responses as they pass through the Django application and web browser.

## **working:**

- The working of middleware in Django involves a series of steps that are followed when requests pass through the middleware components in the applications.
- Middleware is present between the webserver and the view and hooks for pre-processing and post-processing of requests and responses.
    
    
    simple example of middleware
    
    1. functional middleware
        
        ```python
        def simple_funtional_middleware(get_respone):
        		def middleware(request):
        				# Code to be executed for each request before
                # the view (and later middleware) are called.
        				response = get_response(request)
        				# Code to be executed for each request/response after
                # the view is called.
        				return response
        			
        		return middleware
        ```
        
    2. Class middleware
        
        ```python
        class SimpleClassMiddleware:
        		def __init__(self,get_response):
        					self.get_response = get_response
        					# One-time configuration and initialization.
        		def __call__(self,request):
        					# Code to be executed for each request before
        	        # the view (and later middleware) are called.
        					
        					respone = get_response(request)
        					
        					# Code to be executed for each request/response after
        	        # the view is called.
        	        
        	        return response		
        ```
        
        ```python
        MIDDLEWARE = [
        ...
        
        'your_app.middleware_directory.custom_middlewarefile.SimpleClassMiddleware'
        
        ]
        ```
