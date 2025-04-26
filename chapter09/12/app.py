from admin import Admin, Privileges

privileges = Privileges(["can add post", "can delete post", "can ban user"])
admin = Admin('alice','li',23,privileges)

admin.privileges.show_privileges()
admin.greet_user()
