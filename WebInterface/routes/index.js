const express = require('express');
const {spawnSync, spawn} = require('child_process');
const router = express.Router();
const path = require('path');

const protocol = 'UDP';
const protocolDir = path.join(__dirname, '../../' + protocol);
let pyServer = spawn('py', [protocolDir + '/' + protocol + 'server.py']);

pyServer.stderr.on('data', (data) => {
    console.error(data.toString());
});

pyServer.stdout.on('data', (data) => {
    console.log(data.toString());
});

/* GET home page. */
router.get('/', function(req, res, next) {
    res.render('index', { title: 'Computer Network' });
});

function askOpenAI(question) {
    const pyClient = spawnSync('py', [protocolDir + '/' + protocol + 'client.py', question]);
    console.log(pyClient);

    if (pyClient.stdout != null) {
        return pyClient.stdout.toString();
    }

    if (pyClient.stderr != null) {
        console.error(pyClient.stderr.toString());
        return pyClient.stderr.toString();
    }
    return "#####";
}

router.post('/', (req, res  ) => {
    console.log(req.body.content);
    const answer = askOpenAI(req.body.content);
    console.log(answer);
    res.send(answer);
})

module.exports = router;
