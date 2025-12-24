# homebrew

## 术语

## 如何处理依赖？

> 自动处理依赖（递归安装）

> - 当你执行 brew install <package> 时，Homebrew 会解析该软件的所有依赖关系。
>   默认优先使用“二进制包”（Bottle）
> - Homebrew 优先下载官方预编译好的二进制文件，这些文件在 Homebrew 中被称为 Bottles
> - 无需编译：如果你使用的是官方支持的 macOS 或主流 Linux 架构，且安装在默认路径，Homebrew 会直接“倒出”（pour）这些预编译好的包，整个过程像解压一样快，不需要本地编译。
>   什么时候会进行编译
> - Homebrew 才会调用本地编译器（如 Clang 或 GCC）进行现场编译：
> - 无 Bottle 可用：该软件没有为你当前的操作系统版本或硬件架构提供预编译包
> - 使用了 --build-from-source（或简写 -s）参数，强制要求从源代码编译。
> - 在 2025 年，如果你的 macOS 版本已经非常老旧（如不再提供 Bottle 支持的 Tier 3 系统），则大部分安装都会涉及本地编译

## homebrew 处理的内容是什么？

> Homebrew 本身是 Ruby 编写的
>
> Homebrew 经常用于处理 C 语言软件
>
> - 编译 C 软件：很多 Linux/Unix 工具（如 wget, curl, gcc, nginx）都是用 C 语言写的。当你使用 brew install --build-from-source 时，Homebrew 会调用系统中的编译器（如 Apple 的 Clang）来编译这些 C 代码。
> - 安装开发工具：它是 macOS 开发者安装 C 语言编译器（如 GCC）和相关库（如 openssl, libmysqlclient）的最常用工具。
> - 依赖管理：它会自动处理 C 语言项目中复杂的库依赖关系。
