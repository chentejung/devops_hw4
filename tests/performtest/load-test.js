import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  // Define performance thresholds
  thresholds: {
    http_req_failed: ['rate<0.01'], // Error rate must be less than 1%
    http_req_duration: ['p(95)<500'], // 95% of requests must be under 500ms
  },
  stages: [
    { duration: '1m', target: 50 }, // Ramp-up to 50 users
    { duration: '3m', target: 50 }, // Stay at 50 users (Steady state)
    { duration: '1m', target: 0 },  // Ramp-down
  ],
};

export default function () {
  const res = http.get('http://192.168.30.17:5000/filter/cuisine?type=American');
  check(res, { 'status was 200': (r) => r.status == 200 });
  sleep(1);
}