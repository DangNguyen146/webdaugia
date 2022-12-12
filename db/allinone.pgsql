INSERT INTO daugia_memberfee(ID, fee) VALUES (1, 'Paid');
INSERT INTO daugia_memberfee(ID, fee) VALUES (2, 'Unpaid');

INSERT INTO daugia_status(ID, status) VALUES (1, 'Accept');
INSERT INTO daugia_status(ID, status) VALUES (2, 'Pending');
INSERT INTO daugia_status(ID, status) VALUES (3, 'Reject');
INSERT INTO daugia_status(ID, status) VALUES (4, 'Done');

INSERT INTO daugia_result(ID, result) VALUES (1, 'Winner');
INSERT INTO daugia_result(ID, result) VALUES (2, 'Defeat');
INSERT INTO daugia_result(ID, result) VALUES (3, 'notproper');

INSERT INTO daugia_payment(ID, pay) VALUES (1, 'pending');
INSERT INTO daugia_payment(ID, pay) VALUES (2, 'paid');
INSERT INTO daugia_payment(ID, pay) VALUES (3, 'reject');