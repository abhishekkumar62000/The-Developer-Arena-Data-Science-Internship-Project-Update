from src.menu import FinanceManagerApp

def main():
    try:
        app = FinanceManagerApp()
        app.run()
    except KeyboardInterrupt:
        print("\nExiting application safely...")
        app.exit_app()

if __name__ == "__main__":
    main()
