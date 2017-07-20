/*******************************************************************************
* Copyright 2016 ROBOTIS CO., LTD.
*
* Licensed under the Apache License, Version 2.0 (the "License");
* you may not use this file except in compliance with the License.
* You may obtain a copy of the License at
*
*     http://www.apache.org/licenses/LICENSE-2.0
*
* Unless required by applicable law or agreed to in writing, software
* distributed under the License is distributed on an "AS IS" BASIS,
* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
* See the License for the specific language governing permissions and
* limitations under the License.
*******************************************************************************/

/* Authors: Darby Lim */

#ifndef MINIMUM_JERK_H_
#define MINIMUM_JERK_H_

#include "calc.h"

namespace open_manipulator
{
typedef struct
{
  float pos;
  float vel;
  float acc;
} Property;

class MinimumJerk
{
 public:
  Eigen::MatrixXf coeffi_;

 public:
  MinimumJerk(Property* start, Property* end, uint8_t target_num, float mov_time, float control_period);
  ~MinimumJerk();

  void getPosition(float* pos, uint8_t to, float tick);
  void getVelocity(float* vel, uint8_t to, float tick);
  void getAcceleration(float* acc, uint8_t to, float tick);
};
}

#endif // MINIMUM_JERK_H_