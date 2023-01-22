const mineflayer = require('mineflayer');

console.log('Starting...')

function createBot () {
    const bot = mineflayer.createBot({
    host: "debaybr0.aternos.me",
    port: "18822",
    username:"Bot",
    version: 1.19
    })
    bot.on('login', function() {
      bot.chat('/login 123123123 123123123')
    })
    bot.on('chat', (username, message) => {
      if (username === bot.username) return
      target = bot.players[username].entity
      let entity
      switch (message) {
        case ';start':
          bot.setControlState('forward', true)
          bot.setControlState('jump', true)
          bot.setControlState('sprint', true)
          break
          case ';stop':
            bot.clearControlStates()
            break
          }
        })
        bot.on('spawn', function() {
          bot.chat('Spawned')
        })
        bot.on('death', function() {
          bot.chat('I died, respawn')
        })
        bot.on('kicked', (reason, loggedIn) => console.log(reason, loggedIn))
        bot.on('error', err => console.log(err))
        bot.on('end', createBot)
}
createBot()
