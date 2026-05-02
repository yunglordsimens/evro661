import { artists } from './artists.js'
import { illustrations } from './illustrations.js'

export { artists } from './artists.js'
export { illustrations } from './illustrations.js'
export { eventConfig } from './config.js'

// Builds the flat array AppLineup expects:
// artists in block order with illustration dividers inserted at the right spots.
function buildLineup() {
  const result = []
  const blocks = [...new Set(artists.map((a) => a.block))].sort()

  blocks.forEach((blockNum) => {
    result.push(...artists.filter((a) => a.block === blockNum))
    const divider = illustrations.find((i) => i.afterBlock === blockNum)
    if (divider) result.push(divider)
  })

  return result
}

export const lineupData = buildLineup()
