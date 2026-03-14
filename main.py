# Secure Bot Code

class SecureBot:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f'Hello, I am {self.name}, your secure bot.'

    def secure_action(self, action):
        # Add security checks here
        if self.check_permission(action):
            return f'Action {action} has been performed securely.'
        return 'Permission denied.'

    def check_permission(self, action):
        # Basic permission logic
        return action in ['read', 'write']

# Example usage of SecureBot
if __name__ == '__main__':
    bot = SecureBot('Guardian')
    print(bot.greet())
    print(bot.secure_action('write'))
    print(bot.secure_action('delete'))