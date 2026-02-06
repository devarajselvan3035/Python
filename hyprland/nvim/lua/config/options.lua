-- Options are automatically loaded before lazy.nvim startup
-- Default options that are always set: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/options.lua
-- Add any additional options here
--
vim.g.autoformat = true

vim.opt.number = true
vim.opt.relativenumber = true

vim.keymap.set("n", "<C-R>", ":!python3 %<CR>", { desc = "Run Python File" })
