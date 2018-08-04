# dr
An ed-like client for devRant written in python

## Installation
Clone the repo, cd into it, then run:
```
cd build/
sh ./build-linux.sh #or build-cros.sh if you are using a chromebook
```
For arch users, a non-waterfall version is avalible through AUR. just get the package called `dr` (thanks to @Electrux)
## How to run
Just type `dr` in your terminal and you will be sent straight in to the dr prompt.

## How to log in
Once in the dr prompt, use the command `l`. You will be asked for a username and password. Just follow the prompts.

## How to make a post
First, you should be logged in (see above)

In dr, post creation is done in these steps:
 - Create a new rant
 - Add tags to the rant
 - Post the rant
Here is how to do that:

### Create a new rant
To create a new rant, use the command `r`. You will notice that the prompt changes. (The `|` prompt means that you are in rant mode and the `>` prompt means you are in command mode.) You can now type out your rant. But be careful! Once you move to the next line, you can not go back to an old line and fix a mistake. You will have to rewrite the rant (TODO: Fix this). Once you are done, move to a new line, and type `.` then press enter.

### Add tags
To add tags to your rant, use the command `t`. The prompt will go back to the rant prompt and ask you for tags. Type out your tags, then press enter.

### Post the rant
Make sure you have logged in before continuing with this step.
To post the rant you have just created, use the `p` command. You will be asked for verification. That's it! You have posted your first rant using the dr client!

## Viewing a rant
To view a rant, use the command `v`. To view the next rant, use the command `v+`. To view the previous rant, use the command `v-`.

To change the rant feed you are reading from, use the `s` command followed by the code for the feed you want.

Feed list
 - t = top
 - a = algo
 - r = recent

So. to view the top rants, use the command `st` and to view the algo, use `sa`

## Check Your Notifs
To see your notifications, use the command `n`. They will all show up on your screen. In each notif, there is a rantCode. This will be important for later.

(In a future release, you will be able to clear your notifs with the command `n!`)

## Viewing a Rant From It's rantCode
To view a specific rant in dr, you must know it's rantCode. These codes are displayed in your notifications feed and will soon be displayed on all rants.

A rantCode is a stripped down hexadecimal representation of the rant it refers to. It was created because the normal devRant rant ids are getting too long to remember. The current method of creating rantCodes is quite flawed and will soon be   replaced.

To view a rant from its rantCode, use the command `vi`. You will then be prompted for a rantCode. After entering the code, the rant you wanted to see will be shown.
