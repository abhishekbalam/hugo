# Introduction

I wanted to make a personal chatbot to help me out with basic tasks like push my repos to GitHub or update my sites for me.

# Working

This project is basically a chatbot based on AIML, a tool which was initally made for the A.L.I.C.E bot.

AIML is a markup language, similar to XML, which is at the core of the application.

It is used to define the responses to questions as given below:

<samp>

    <category>
    <pattern>HELLO</pattern>
    <template>
        Well, hello!
    </template>
    </category>
    <category>
        <pattern>WHAT ARE YOU</pattern>
        <template>
            I'm a bot, silly!
        </template>
    </category>
    <category>
        <pattern>HOW DID I *</pattern>
        <template>
        <random>
            <li>I'm not sure I wasn't paying a bit of attention</li>
            <li>Well you see</li>
            <li>I do not recall</li>
        </random>
        </template>
    </category>
</samp>

# Features

This project was supposed to be more comprehensive and had more features.

The bot has the following features:
- Add features as modules
- Add responses by adding more custom AIML
- CLI interface
- binary available.


# Conclusion

This project still has some work to do, but I'll finish it in the future.
