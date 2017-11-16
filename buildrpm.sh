name=hiredis
version=13.3
release=1
rpmdir=${PWD}/.RPMBUILD
mkdir -p ${rpmdir}
rm -rf ${rpmdir}/*

tar zcvf ${rpmdir}/${name}-${version}-${release}.tar.gz *

cd ${rpmdir}

# 通过tar包构建rpm包，似乎不需要指定sourcedir和specdir
                #--define="_sourcedir ${rpmdir}/source"  \
                #--define="_specdir ${rpmdir}/spec"    \
rpmbuild -tb --define="_topdir ${rpmdir}" \
                --define="_builddir ${rpmdir}/build"   \
                --define="_buildrootdir ${rpmdir}/buildroot"   \
                --define="_rpmdir ${rpmdir}/rpm"       \
                --define="_srcrpmdir ${rpmdir}/srcrpm" \
                --define="name ${name}" \
                --define="version ${version}" \
                --define="release ${release}" \
                ${name}-${version}-${release}.tar.gz
