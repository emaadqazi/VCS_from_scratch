## The end goals for this project

1) Content-addressable object storage
- the foundation of Git 
- need to take some content and hash it (SHA-1)
- this gives us deduplication and integrity checking for free, mirroring Git's checksumming process

2) 3 object types
- blob (raw contents)
- tree; directory listing that maps filenames to the hashes of their blobs or sub-trees
- commit; points to one tree, points to a parent commit, and carries the message/timestamp/author. This is important as commits in Git tell us: here is the snapshot, here is what came before it, and this allows for the whole stream of snapshots idea that Git relies on

3) Staging area 
- the `add` command should hash the file's current content, store it as a blob, and record that mapping in the staging file. This allows us to go from "change" to "commit"

4) The commit command
- turns the staging area into a tree object
- creates a commit object pointing to that tree and to the current HEAD 
- then stores it and moves HEAD to point at the new commit 
- this will be the working bare bones of the VSC system

5) References (HEAD and branches)
- branch is just a small file containing a commit hash 
- HEAD is a pointer to a branch 

6) Inspection commands
- log, status, checkout, etc.
- log: walks the parent pointers from HEAD backwards
- status: compares working directory vs staging area vs last commit
- checkout: needs to read a tree object and rewrite the working directory to match it

# What v1 will be missing:
1) No merging
2) No diff algorithm
3) No remotes 

# Focus
Focus is on getting the:
init -> add -> commit -> log -> checkout
Functionality working