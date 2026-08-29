# V82QSS AWS launch ledger

Launched 2026-08-26 08:11:05Z from source archive SHA-256
`74b69deb04c36c4aa4f3a81ad1720704c2b9132b8a89cd35d594780428ae582b`.
The launcher SHA-256 is
`899ed73e713b17fd294a970d08ccb211ad1c61cee12d9847935e807eec8535c9`.

Both hosts passed the Linux/Amazon-EC2/archive/RAM preflight.  Each q11/q16
lane has a 4 GiB address-space cap and 10,800-second timeout.

## Box03

- host `98.80.65.144`, hostname `ip-172-30-0-249`;
- run root
  `/home/ubuntu/runs/td6_v82qss_symbol_box03_20260826T081053Z`;
- supervisor PID `183839`;
- lane wrapper PIDs q11=`183843`, q16=`183851`;
- Python PIDs at startup q11=`183863`, q16=`183865`.

## r6d

- host `100.26.198.153`, hostname `ip-172-30-0-45`;
- run root
  `/home/ubuntu/runs/td6_v82qss_symbol_r6d_20260826T081053Z`;
- supervisor PID `249330`;
- lane wrapper PIDs q11=`249334`, q16=`249342`;
- Python PIDs at startup q11=`249354`, q16=`249356`.

All four lanes verified the frozen source closure and entered exact transport.
No result is interpreted before terminal rc, dual-host expression agreement,
and the preregistered full/omit/gauge controls.
