// Copyright 2016 Proyectos y Sistemas de Mantenimiento SL (eProsima).
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

/*!
 * @file Move.h
 * This header file contains the declaration of the described types in the IDL file.
 *
 * This file was generated by the tool gen.
 */

#ifndef _FAST_DDS_GENERATED_MOVE_H_
#define _FAST_DDS_GENERATED_MOVE_H_


#include <stdint.h>
#include <array>
#include <string>
#include <vector>
#include <map>
#include <bitset>

#if defined(_WIN32)
#if defined(EPROSIMA_USER_DLL_EXPORT)
#define eProsima_user_DllExport __declspec( dllexport )
#else
#define eProsima_user_DllExport
#endif  // EPROSIMA_USER_DLL_EXPORT
#else
#define eProsima_user_DllExport
#endif  // _WIN32

#if defined(_WIN32)
#if defined(EPROSIMA_USER_DLL_EXPORT)
#if defined(Move_SOURCE)
#define Move_DllAPI __declspec( dllexport )
#else
#define Move_DllAPI __declspec( dllimport )
#endif // Move_SOURCE
#else
#define Move_DllAPI
#endif  // EPROSIMA_USER_DLL_EXPORT
#else
#define Move_DllAPI
#endif // _WIN32

namespace eprosima {
namespace fastcdr {
class Cdr;
} // namespace fastcdr
} // namespace eprosima


/*!
 * @brief This class represents the structure Move defined by the user in the IDL file.
 * @ingroup MOVE
 */
class Move
{
public:

    /*!
     * @brief Default constructor.
     */
    eProsima_user_DllExport Move();

    /*!
     * @brief Default destructor.
     */
    eProsima_user_DllExport ~Move();

    /*!
     * @brief Copy constructor.
     * @param x Reference to the object Move that will be copied.
     */
    eProsima_user_DllExport Move(
            const Move& x);

    /*!
     * @brief Move constructor.
     * @param x Reference to the object Move that will be copied.
     */
    eProsima_user_DllExport Move(
            Move&& x);

    /*!
     * @brief Copy assignment.
     * @param x Reference to the object Move that will be copied.
     */
    eProsima_user_DllExport Move& operator =(
            const Move& x);

    /*!
     * @brief Move assignment.
     * @param x Reference to the object Move that will be copied.
     */
    eProsima_user_DllExport Move& operator =(
            Move&& x);

    /*!
     * @brief Comparison operator.
     * @param x Move object to compare.
     */
    eProsima_user_DllExport bool operator ==(
            const Move& x) const;

    /*!
     * @brief Comparison operator.
     * @param x Move object to compare.
     */
    eProsima_user_DllExport bool operator !=(
            const Move& x) const;

    /*!
     * @brief This function sets a value in member ismoving
     * @param _ismoving New value for member ismoving
     */
    eProsima_user_DllExport void ismoving(
            uint32_t _ismoving);

    /*!
     * @brief This function returns the value of member ismoving
     * @return Value of member ismoving
     */
    eProsima_user_DllExport uint32_t ismoving() const;

    /*!
     * @brief This function returns a reference to member ismoving
     * @return Reference to member ismoving
     */
    eProsima_user_DllExport uint32_t& ismoving();

    /*!
     * @brief This function sets a value in member index
     * @param _index New value for member index
     */
    eProsima_user_DllExport void index(
            uint32_t _index);

    /*!
     * @brief This function returns the value of member index
     * @return Value of member index
     */
    eProsima_user_DllExport uint32_t index() const;

    /*!
     * @brief This function returns a reference to member index
     * @return Reference to member index
     */
    eProsima_user_DllExport uint32_t& index();


    /*!
     * @brief This function returns the maximum serialized size of an object
     * depending on the buffer alignment.
     * @param current_alignment Buffer alignment.
     * @return Maximum serialized size.
     */
    eProsima_user_DllExport static size_t getMaxCdrSerializedSize(
            size_t current_alignment = 0);

    /*!
     * @brief This function returns the serialized size of a data depending on the buffer alignment.
     * @param data Data which is calculated its serialized size.
     * @param current_alignment Buffer alignment.
     * @return Serialized size.
     */
    eProsima_user_DllExport static size_t getCdrSerializedSize(
            const Move& data,
            size_t current_alignment = 0);


    /*!
     * @brief This function serializes an object using CDR serialization.
     * @param cdr CDR serialization object.
     */
    eProsima_user_DllExport void serialize(
            eprosima::fastcdr::Cdr& cdr) const;

    /*!
     * @brief This function deserializes an object using CDR serialization.
     * @param cdr CDR serialization object.
     */
    eProsima_user_DllExport void deserialize(
            eprosima::fastcdr::Cdr& cdr);



    /*!
     * @brief This function returns the maximum serialized size of the Key of an object
     * depending on the buffer alignment.
     * @param current_alignment Buffer alignment.
     * @return Maximum serialized size.
     */
    eProsima_user_DllExport static size_t getKeyMaxCdrSerializedSize(
            size_t current_alignment = 0);

    /*!
     * @brief This function tells you if the Key has been defined for this type
     */
    eProsima_user_DllExport static bool isKeyDefined();

    /*!
     * @brief This function serializes the key members of an object using CDR serialization.
     * @param cdr CDR serialization object.
     */
    eProsima_user_DllExport void serializeKey(
            eprosima::fastcdr::Cdr& cdr) const;

private:

    uint32_t m_ismoving;
    uint32_t m_index;
};

#endif // _FAST_DDS_GENERATED_MOVE_H_