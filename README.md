      # airflow
      Запуск сервиса provider_a
      uvicorn provider_a:app --reload --port 8990

      Запуск сервиса provider_b
      uvicorn provider_b:app --reload --port 8991
