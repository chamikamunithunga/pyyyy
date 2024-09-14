# Import necessary modules
import mojo

# Create a simple web server
class MyApp(mojo.Application):
    def get(self):
        return "Hello, Web World!"

# Run the server
if __name__ == "__main__":
    app = MyApp()
    app.run()
