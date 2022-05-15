# git操作指北

## 基本操作

1. cd进入特定目录或者直接Git bash here。把当前目录变成一个git可以管理的仓库：

     git init                      # 初始化git仓库

2. 添加文件

     git add fileName              # 向git添加单个文件到暂存区，而没有向仓库提交，仓库内文件不发生变化，直到commit
     git add -A                    # 向git添加全部文件到git，一般最好不用it

3. 提交修改

     git commit -m "You commit"    # 为你向git仓库的提交添加备注，同时让暂存区的修改提交到仓库

4. 查看暂存区是否有未提交修改

     git status                    # 查看仓库状态

5. 查看最近日志

     git log                       # 查看仓库近期修改

6. 版本回退操作

     git reset -hard HEAD^         # 回退一个，当然也可以用ID回退
     git reset -hard HEAD^         # 回退两个
     git reset -hard HEAD~100      # 回退多个

7. 第一个连接远程仓库

    git remote add origin yourRemoteUrl  # 第一个远程提交
    git push -u origin master            # 仓库关联git

8. 第二次及以后提交

     git push                           # 代码提交

9. 建立、查看、删除分支

     git branch your_new_branch               # 向仓库添加一个新的分支 git branch slave  新建slave分支，但建完之后仍在master分支
     git checkout your_branch                 # 转换到你的分支，用git checkout命令
     git branch -a                            # 查看所有分支
     git push origin --delete dele_branch     # 删除分支

## Tips:常见报错

- [rejected] master -> master (fetch first)
可能在不同的机器上上做了提交？？远程分支上存在本地分支中不存在的提交，往往是多人协作开发过程中遇到的问题，可以先fetch再merge，也就是pull，
把远程分支上的提交合并到本地分支之后再push。如果你确定远程分支上那些提交都不需要了，那么直接
git push origin master -f
强行让本地分支覆盖远程分支。

- error: failed to push some refs
可以使用
git pull --rebase origin master          # 把远程仓库的最新文件下载下来
然后push

     git push origin master

- The current branch test has no upstream branch.

     git push --set-upstream origin test

- 使用ssh, 最好不适用https
