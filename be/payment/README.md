Minimal Spring Boot payment service.

Build and run:
  cd be/payment
  mvn package
  java -jar target/payment-0.1.0.jar

Endpoints:
  POST /api/payments          -> create payment (JSON: { "amount": 10.5, "currency": "USD" })
  GET  /api/payments          -> list payments
  GET  /api/payments/{id}     -> get payment
  POST /api/payments/{id}/capture -> mark payment captured