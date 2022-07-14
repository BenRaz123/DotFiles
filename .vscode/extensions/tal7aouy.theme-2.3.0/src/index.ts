import { build } from '~/scripts/build'
import { pressEnterToExit } from '~/utils/press-enter-to-exit'
import Theme from '~/variants/theme'
import ThemeFlat from '~/variants/ThemeFlat'
import { ThemeItalics } from '~/variants/themeItalic'

async function run() {
  await build(Theme)
  await build(ThemeItalics)
  await build(ThemeFlat)

  if (process.env.DEBUG_VSCODE) {
    pressEnterToExit() // Hold the process alive
  }
}

run()
