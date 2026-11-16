# Inbox

Drop a new post here as plain markdown (or .txt) and push to `master`.

```
# My Post Title
Tags: space, robots
Summary: Optional one-liner for the homepage.

Write whatever you want...
```

`Tags:` and `Summary:` are optional, must come right after the title, and are
removed from the post body. Tags can be comma- or space-separated.

A GitHub Action will:

- use the `# Heading` line as the title (or the filename, if there's no heading)
- date it today (or keep a `YYYY-MM-DD-` prefix if the filename has one)
- add the front matter and move it to `_posts/`
- trigger a Pages build

Need tags or a custom summary? Add front matter yourself and it will be left alone.
After pushing a post, `git pull` before the next one (the Action commits back).
