# Lookahead

Positive lookahead for *bar* infront of `foo`:

	foo\(bar\)\@=

Negative lookahead for *bar* infront of foo
That is only match 'foo's that do not have bar immediately infront

    foo\(bar\)\@!

    Anywhere infront:

        foo\(.*bar\)\@!

# Lookbehind

foo's that do not have a pound sign anywhere before them on a line

    \(#.*\)\@<!foo
