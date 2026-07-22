FROM ubuntu:22.04

RUN apt-get update && apt-get install -y python3 sudo && rm -rf /var/lib/apt/lists/*

COPY gotify /usr/local/bin/gotify
RUN chmod +x /usr/local/bin/gotify

RUN echo 'root ALL=(ALL) NOPASSWD: /usr/sbin/shutdown' > /etc/sudoers.d/gotify-shutdown

COPY test_cmd.py /tmp/test_cmd.py

CMD ["/bin/bash"]
