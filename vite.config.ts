import { defineConfig } from 'vite'
import { execSync } from 'child_process'

const gitDate = execSync('git log -1 --format="%cd" --date=format:"%Y.%m.%d"')
  .toString()
  .trim()

export default defineConfig({
  define: {
    __GIT_DATE__: JSON.stringify(gitDate),
  },
  assetsInclude: ['**/*.xlsx'],
})
