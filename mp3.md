# MP3

Use `easytag` (gui)

## Track listing padded number

    for x in *.mp3; do mv "$x" "`mp3info -p "%02n" "$x"`-$x"; done
