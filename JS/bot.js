const mineflayer = require('mineflayer');

console.log('Starting...')

function createBot () {
    const bot = mineflayer.createBot({
    host: "mineprosLET.aternos.me",
    port: "18009",
    username: "Admins",
    version: false
    })
    bot.on('login', function() {
      bot.chat('/reginster bot228bot228 bot228bot228')
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
          bot.chat('Заспавнялся')
        })
        bot.on('death', function() {
          bot.chat('Я умер,Респавнюсь')
        })
        bot.on('kicked', (reason, loggedIn) => console.log(reason, loggedIn))
        bot.on('error', err => console.log(err))
        bot.on('end', createBot)
}
createBot()
