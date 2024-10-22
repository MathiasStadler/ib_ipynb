
class TestApp():
    def get_name(_):
        print("inside")
        return "get_name so stupid"
        

def main():
    print("Hello python");

    app=TestApp()
    request = app.get_name()
    print(request)



if __name__ == "__main__":
    main() 