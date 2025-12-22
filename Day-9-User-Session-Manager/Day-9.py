# Day 9 - User Session Manager
# Focus: Hashing
# Language: Python 3

import time


class SessionManager:
    def __init__(self):
        # user_id -> last_active_timestamp
        self.sessions = {}

    def login(self, user_id):
        self.sessions[user_id] = time.time()
        print(f"User {user_id} logged in.")

    def logout(self, user_id):
        if user_id in self.sessions:
            del self.sessions[user_id]
            print(f"User {user_id} logged out.")
        else:
            print("User not logged in.")

    def is_active(self, user_id, timeout=300):
        """
        Checks if user session is active within timeout (seconds)
        """
        if user_id not in self.sessions:
            return False

        return (time.time() - self.sessions[user_id]) <= timeout

    def cleanup_expired_sessions(self, timeout=300):
        current_time = time.time()
        expired_users = [
            user for user, last_active in self.sessions.items()
            if current_time - last_active > timeout
        ]

        for user in expired_users:
            del self.sessions[user]

        print(f"Cleaned up {len(expired_users)} expired sessions.")

    def show_sessions(self):
        print("\nActive Sessions:")
        for user in self.sessions:
            print(f"- {user}")


def main():
    sm = SessionManager()

    sm.login("alice")
    sm.login("bob")

    time.sleep(2)

    print("Is Alice active?", sm.is_active("alice"))
    print("Is Bob active?", sm.is_active("bob"))

    sm.logout("alice")
    sm.cleanup_expired_sessions()

    sm.show_sessions()


if __name__ == "__main__":
    main()
