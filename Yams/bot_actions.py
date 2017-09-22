#!/usr/bin/env python
# -*- coding: utf-8 -*-
# made with python 3
"""Main"""
from disco.bot import Plugin


class SimplePlugin(Plugin):
    # They also provide an easy-to-use command component
    @Plugin.command('/ping')
    def on_ping_command(self, event):
        event.msg.reply('Pong!')

    # Which includes command argument parsing
    @Plugin.command('/echo', '<content:str...>')
    def on_echo_command(self, event, content):
        event.msg.reply(content)

    @Plugin.command('/help')
    def help_command(self, event):
        event.msg.reply("/echo, te responde con lo que pongas a continuación\n" +
                         "/ping, te responde con un friendly pong para saber si está encendido el bot")
